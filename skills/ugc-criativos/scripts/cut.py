import sys, cv2, numpy as np, subprocess, os
from rembg import remove, new_session
sess=new_session('u2net_human_seg') if os.path.exists(os.path.expanduser('~/.u2net/u2net_human_seg.onnx')) else new_session('u2net')
src,out=sys.argv[1],sys.argv[2]
cap=cv2.VideoCapture(src); fps=cap.get(5)
os.makedirs(out,exist_ok=True); i=0
while True:
    ok,f=cap.read()
    if not ok: break
    small=cv2.resize(f,(540,960))
    m=remove(small,session=sess,only_mask=True)
    m=cv2.resize(np.array(m),(f.shape[1],f.shape[0]))
    m=cv2.GaussianBlur(m,(7,7),0)
    rgba=np.dstack([f,m]); cv2.imwrite(f'{out}/{i:04d}.png',rgba); i+=1
print(src,i,fps)
