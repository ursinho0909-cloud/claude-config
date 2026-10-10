import sys, cv2, numpy as np, os
from rembg import remove, new_session
sess = new_session(sys.argv[3] if len(sys.argv) > 3 else 'u2net_human_seg')
src, out = sys.argv[1], sys.argv[2]
cap = cv2.VideoCapture(src); os.makedirs(out, exist_ok=True); i = 0
while True:
    ok, f = cap.read()
    if not ok: break
    m = np.array(remove(cv2.resize(f, (540, 960)), session=sess, only_mask=True)).astype(np.float32)
    m = np.clip((m - 90) / (190 - 90), 0, 1) * 255          # corta fantasmas semi-transparentes
    m = cv2.resize(m.astype(np.uint8), (f.shape[1], f.shape[0]))
    m = cv2.GaussianBlur(m, (7, 7), 0)
    cv2.imwrite(f'{out}/{i:04d}.png', np.dstack([f, m])); i += 1
print(src, i)
