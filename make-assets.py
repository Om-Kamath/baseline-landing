from pathlib import Path
p=Path(__file__).parent/'dist/assets'
def text(x,y,s,size=16,color='#fff',weight=400):
 return f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" font-weight="{weight}" font-family="Arial,sans-serif">{s}</text>'
def card(x,y,w,h):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="27" fill="white" fill-opacity=".12" stroke="white" stroke-opacity=".2"/>'
def head(title):return f'''<svg xmlns="http://www.w3.org/2000/svg" width="390" height="844" viewBox="0 0 390 844"><defs><radialGradient id="a"><stop stop-color="#77671b"/><stop offset="1" stop-color="#77671b" stop-opacity="0"/></radialGradient><radialGradient id="b"><stop stop-color="#642c78"/><stop offset="1" stop-color="#642c78" stop-opacity="0"/></radialGradient><radialGradient id="c"><stop stop-color="#225e58"/><stop offset="1" stop-color="#225e58" stop-opacity="0"/></radialGradient><linearGradient id="charge"><stop stop-color="#fb5a5c"/><stop offset=".5" stop-color="#f6cf49"/><stop offset="1" stop-color="#b5e66b"/></linearGradient></defs><rect width="390" height="844" fill="#13202e"/><ellipse cx="40" cy="210" rx="430" ry="550" fill="url(#a)"/><ellipse cx="410" cy="440" rx="380" ry="490" fill="url(#b)"/><ellipse cx="120" cy="800" rx="400" ry="480" fill="url(#c)"/>{text(27,34,'9:41',13,weight=700)}<path d="M312 29h3m4-3v3m5-6v6" stroke="white" stroke-width="3"/><path d="M335 25q8-7 16 0m-13 4q5-4 10 0" fill="none" stroke="white" stroke-width="2"/><rect x="360" y="22" width="17" height="9" rx="3" fill="white"/>{text(23,99,title,32,weight=700)}'''
def chart(y,color='#8bec95'):
 s=''
 for i in range(4):s+=f'<path d="M40 {y+i*40}H350" stroke="white" stroke-opacity=".12"/>'
 s+=f'<path d="M43 {y+99} C80 {y+90},95 {y+100},125 {y+65} S180 {y+80},210 {y+45} S270 {y+51},300 {y+29} S332 {y+24},350 {y+9}" fill="none" stroke="{color}" stroke-width="4" stroke-linecap="round"/>'
 return s
s=head('Baseline')+card(16,125,358,175)
s+=f'<circle cx="104" cy="211" r="62" fill="none" stroke="#f3dc51" stroke-opacity=".2" stroke-width="13"/><circle cx="104" cy="211" r="62" fill="none" stroke="#f3dc51" stroke-width="13" stroke-dasharray="275 390" transform="rotate(-90 104 211)" stroke-linecap="round"/>'
s+=text(72,225,'72',43,weight=700)+text(190,179,'♥  Recovery',14,'#e6e8c2')+text(190,211,'●  Good',20,'#fff',700)+text(190,241,'Ready for your day.',12,'#d0d6c5')+text(190,262,'A little above your usual.',11,'#d0d6c5')
s+=card(16,316,358,135)+text(35,348,'ϟ  Body Charge',14,'#d8e8c9')+text(35,393,'80',34,weight=700)+text(91,391,'High',14,'#d8dfc9')+text(228,348,'+8 since waking',11,'#c3c8c6')+'<rect x="35" y="415" width="320" height="12" rx="6" fill="white" fill-opacity=".15"/><rect x="35" y="415" width="264" height="12" rx="6" fill="url(#charge)"/>'
for x,label,value,color,usual in [(16,'☾  Sleep','7h 42m','#a9a2ff','Usual 7h 18m'),(203,'⌁  HRV','85 ms','#f2799d','Usual 82 ms')]:
 s+=card(x,467,171,168)+text(x+18,499,label,14,color)+text(x+18,538,value,27,weight=700)+text(x+18,563,usual,11,'#c6cbd0')
 for i,h in enumerate([26,21,31,24,20,30,34]):s+=f'<rect x="{x+18+i*20}" y="{615-h}" width="14" height="{h}" rx="7" fill="{color}" opacity="{1 if i==6 else .45}"/>'
s+=card(16,652,358,170)+text(35,685,'Last 7 Days',18,weight=700)+text(294,685,'Avg 68',11,'#c6cbd0')+chart(705,'#75b5ff')
s+='<rect x="135" y="831" width="120" height="4" rx="2" fill="white"/></svg>'
(p/'screenshot-dashboard.svg').write_text(s)
s=head('Body Charge')+card(16,125,358,226)+text(36,160,'ϟ  Your energy, right now',15,'#b5efb1')+text(36,227,'80',58,weight=700)+text(125,226,'High',20,'#d0decc')+'<rect x="36" y="253" width="317" height="14" rx="7" fill="white" fill-opacity=".15"/><rect x="36" y="253" width="260" height="14" rx="7" fill="url(#charge)"/>'+text(36,303,'Find your rhythm.',16,weight=700)+text(36,326,'Activity spends energy. Rest brings it back.',11,'#d1d3ce')
s+=card(16,369,358,260)+text(36,406,'Today’s timeline',19,weight=700)+chart(437)+text(41,592,'8 AM',10,'#c6cbd0')+text(172,592,'12 PM',10,'#c6cbd0')+text(307,592,'4 PM',10,'#c6cbd0')
s+=card(16,647,358,158)+text(36,680,'Today so far',18,weight=700)
for x,v,l in [(36,'72','Started'),(149,'80','Now'),(267,'+8','Change')]:s+=text(x,732,v,31,weight=700)+text(x,761,l,12,'#d2d6cb')
s+='</svg>';(p/'screenshot-body-charge.svg').write_text(s)
s=head('Recovery')+card(16,125,358,208)+text(36,163,'YOUR MORNING CHECK-IN',11,'#d3dfc8',700)+text(36,239,'72',70,weight=700)+text(140,225,'Good recovery',20,'#e9e47a',700)+text(36,291,'Measured against your normal.',14,'#d5dbd3')
s+=card(16,351,358,411)+text(36,391,'Behind your score',20,weight=700)
for i,(label,val,col,percent) in enumerate([('Heart rate variability','85 ms','#f48fae',.85),('Sleep','7h 42m','#b6aeff',.77),('Resting heart rate','52 bpm','#82c7ff',.7),('Breathing rate','14 /min','#8ee4b0',.8),('Wrist temperature','+0.1°','#efcb83',.9)]):
 y=436+i*63;s+=text(36,y,label,13,'#e1e5dd')+text(281,y,val,13,weight=700)+f'<rect x="36" y="{y+15}" width="316" height="6" rx="3" fill="white" fill-opacity=".1"/><rect x="36" y="{y+15}" width="{316*percent}" height="6" rx="3" fill="{col}"/>'
s+=text(37,804,'Your body. Your baseline.',13,'#d5dbd3')+'</svg>';(p/'screenshot-recovery.svg').write_text(s)
s=head('Sleep')+card(16,125,358,159)+text(36,160,'☾  Last night',15,'#bcb3ff')+text(36,214,'7h 42m',44,weight=700)+text(36,251,'Usual 7h 18m',14,'#d3d9d2')+card(16,302,358,302)+text(36,342,'A closer look at your night',18,weight=700)
for i,(l,c) in enumerate([('Awake','#f5ce82'),('REM','#82e3ed'),('Core','#5ba6ff'),('Deep','#9c91fa')]):
 y=380+i*43;s+=text(36,y+12,l,11,'#d2d5d7')+f'<path d="M87 {y+21}H352" stroke="white" stroke-opacity=".12"/>'
 for j in range(7):
  if (j+i)%3!=0:s+=f'<rect x="{89+j*37}" y="{y}" width="{12+((i+j)%3)*7}" height="18" rx="4" fill="{c}"/>'
s+=text(87,571,'11 PM',10,'#d2d5d7')+text(201,571,'3 AM',10,'#d2d5d7')+text(321,571,'7 AM',10,'#d2d5d7')
for x,v,l in [(16,'96%','Efficiency'),(203,'1h 48m','Deep sleep')]:s+=card(x,622,171,133)+text(x+20,659,l,14,'#d2d5d7')+text(x+20,710,v,30,weight=700)
s+=text(36,801,'More than hours. Real insight.',14,'#d5dbd3')+'</svg>';(p/'screenshot-sleep.svg').write_text(s)
(p/'favicon.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="17" fill="#111"/><text x="16" y="49" font-family="Arial" font-weight="900" font-size="52" fill="#FAF8F3">b</text><circle cx="48" cy="47" r="5" fill="#b8a0e9"/></svg>')
