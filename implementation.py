import time,sys;from random import randint as rint;import curses as h;w=h.initscr();
h.noecho();h.cbreak()
rs,cs,m,s,e,p,a,q=20,10,5,300,{0:"  ",1: "\u2588"*2},[[[1,1],[1,1]],[[0,1,0],[1]*3,[0]
*3],[[1,0,0],[1]*3,[0]*3],[[0,0,1],[1]*3,[0]*3],[[1,1,0],[0,1,1],[0]*3],[[0,1,1]
,[1,1,0],[0]*3],[[0]*4,[1]*4,[0]*4,[0]*4]],range,len;
p=[[[[px,i+1]for px in r] for r in b]for(i,b)in enumerate(p)]
cu,b,f,t=p[rint(0,6)],[[[0,0]]*cs for r in a(rs)],False,True;
y,ro,co,cr,l,d,n=lambda z,x,y,e=e:(e[z[x][y][0]],z[x][y][1]),0,cs//2,0,1,s,p[rint(0,6)];
w.nodelay(t);w.keypad(t);h.curs_set(f);h.start_color();
for j in a(1,8):h.init_pair(j,j,0)
def c_c(ro, co, se):
 for (r,c) in [(r,c) for c in a(q(cu)) for r in a(q(cu))]:
  if se[r][c][0]==1 and(ro+r<0 or ro+r>=rs or co+c<0 or co+c>=cs):return f
  if se[r][c][0]==1 and b[ro+r][co+c][0]+se[r][c][0]>1:return f
 return True
def m_d():
 global ro,co,cu,n,l,d;v,g=lambda cu=cu:cu[r][c][0]>0,lambda j,b=b:sum(px[0]for px in b[j])==cs
 if not c_c(ro+1,co,cu):
  if ro==0:raise Exception("Game over!")
  for (r,c) in [(r,c)for c in a(q(cu))for r in a(q(cu))]:
   if ro+r in a(rs)and co+c in a(cs)and v():b[ro+r][co+c]=cu[r][c]
  cu,n,ro,co,d=n,p[rint(0,6)],-1,cs//2,s+m-l*m
  for i in[j for j in a(rs)if g(j)]:b[1:i+1]=b[:i];b[0],l=[[0,0]]*cs,l+1
try:
 while True:
  w.move(0,0);o=a(q(n));u=[(r,c) for c in a(q(cu)) for r in a(q(cu))]
  for (r,c) in [(r,c) for c in a(cs) for r in a(rs)]:w.addstr(r,c*q(e),y(b,r,c)[0],h.color_pair(y(b,r,c)[1]))
  w.addstr(rs,0,f"{'='*2*cs}\nLevel: {l}");time.sleep(0.001)
  for(r,c)in[(r,c)for(r,c)in u if cu[r][c][0]==1]:w.addstr(ro+r,(co+c)*2,y(cu,r,c)[0],h.color_pair(y(cu,r,c)[1]))
  for(r,c)in[(r,c)for c in o for r in o]:w.addstr(r,42+c*2,y(n,r,c)[0]+" "*3,h.color_pair(y(n,r,c)[1]))
  try: cr = (cr+1)%d;ch = w.getkey()
  except: ch = None
  if ch=='KEY_DOWN':m_d();ro+=1
  elif ch=='KEY_LEFT'and c_c(ro,co - 1, cu): co -= 1
  elif ch=='KEY_RIGHT'and c_c(ro, co + 1, cu): co += 1
  elif ch=='KEY_UP'and c_c(ro,co,list(zip(*cu[::-1]))):cu=list(zip(*cu[::-1]))
  elif ch=="q":raise Exception("Goodbye!")
  if cr==0: m_d();ro+=1
except Exception as e:
  w.addstr(rs//2,0,f"{e.args[0]:^{2*cs}}\n{'Score: '+str(l):^{2*cs}}",h.color_pair(2));
  w.timeout(-1);w.getch();h.nocbreak();h.echo();w.keypad(f);h.endwin();
