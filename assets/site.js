/* Big Media case studies: motion and interactions. Everything degrades to a static page. */
(function(){
  const $=(s,r=document)=>r.querySelector(s), $$=(s,r=document)=>[...r.querySelectorAll(s)];
  const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;

  // header + scroll progress + hero tilt
  const top=$('.top'), prog=$('.prog'), tilt=$('.tilt');
  function onScroll(){
    const y=scrollY, h=document.documentElement.scrollHeight-innerHeight;
    top&&top.classList.toggle('solid',y>40);
    prog&&(prog.style.width=(h>0?y/h*100:0)+'%');
    if(tilt&&!reduce){const r=tilt.getBoundingClientRect(), p=Math.min(1,Math.max(0,(innerHeight-r.top)/(innerHeight*0.9)));
      tilt.style.transform=`rotateX(${14*(1-p)}deg) scale(${0.94+0.06*p})`;}
  }
  addEventListener('scroll',onScroll,{passive:true}); onScroll();

  // reveal + count-up
  const count=el=>{const end=parseFloat(el.dataset.n);if(isNaN(end)||reduce){return}
    const dur=1300,t0=performance.now();const f=t=>{const p=Math.min(1,(t-t0)/dur),v=end*(1-Math.pow(1-p,3));el.textContent=Math.round(v).toLocaleString('en-AU');if(p<1)requestAnimationFrame(f)};
    el.textContent='0';requestAnimationFrame(f)};
  const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');$$('[data-n]',e.target).forEach(count);if(e.target.dataset.n!==undefined)count(e.target);io.unobserve(e.target)}}),{rootMargin:'0px 0px -8% 0px'});
  $$('.rv,.countme').forEach(el=>io.observe(el));

  // sub-nav active section
  const links=$$('.subnav a[href^="#"]');
  if(links.length){const so=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){links.forEach(a=>a.classList.toggle('on',a.getAttribute('href')==='#'+e.target.id))}}),{rootMargin:'-45% 0px -50% 0px'});
    links.forEach(a=>{const t=$(a.getAttribute('href'));t&&so.observe(t)})}

  // index: cursor preview + filters
  const peek=$('.peek');
  if(peek){const img=$('img',peek);let x=0,y=0,cx=0,cy=0,raf;
    const loop=()=>{cx+=(x-cx)*.18;cy+=(y-cy)*.18;peek.style.left=cx+'px';peek.style.top=cy+'px';raf=requestAnimationFrame(loop)};
    $$('.row').forEach(r=>{r.addEventListener('mouseenter',()=>{img.src=r.dataset.img;peek.style.borderColor=r.style.getPropertyValue('--c');peek.classList.add('on');if(!raf)loop()});
      r.addEventListener('mouseleave',()=>{peek.classList.remove('on')});});
    addEventListener('mousemove',e=>{x=e.clientX+240;y=e.clientY});}
  $$('.chip').forEach(c=>c.addEventListener('click',()=>{$$('.chip').forEach(b=>b.setAttribute('aria-pressed',b===c));
    const f=c.dataset.f;$$('.row').forEach(r=>r.classList.toggle('hide',f!=='all'&&!r.dataset.f.includes(f)))}));

  // gallery drag + arrows
  const strip=$('.strip');
  if(strip){let down=false,sx=0,sl=0,moved=false;
    strip.addEventListener('pointerdown',e=>{if(e.pointerType!=='mouse')return;down=true;moved=false;sx=e.clientX;sl=strip.scrollLeft;strip.classList.add('drag')});
    addEventListener('pointermove',e=>{if(!down)return;const d=e.clientX-sx;if(Math.abs(d)>4)moved=true;strip.scrollLeft=sl-d});
    addEventListener('pointerup',()=>{if(down){down=false;strip.classList.remove('drag')}});
    strip.addEventListener('click',e=>{if(moved){e.preventDefault();e.stopPropagation()}},true);
    $$('.arrows button').forEach(b=>b.addEventListener('click',()=>strip.scrollBy({left:(b.dataset.d==='1'?1:-1)*Math.min(880,innerWidth*.8),behavior:'smooth'})));}

  // lightbox
  const lb=$('.lb');
  if(lb){const shots=$$('[data-zoom]');let i=0;const im=$('img',lb),cap=$('.cap',lb);
    const show=k=>{i=(k+shots.length)%shots.length;im.src=shots[i].dataset.zoom;cap.textContent=shots[i].dataset.cap||'';lb.classList.add('on');document.body.style.overflow='hidden'};
    const hide=()=>{lb.classList.remove('on');document.body.style.overflow=''};
    shots.forEach((s,k)=>s.addEventListener('click',()=>show(k)));
    $('.x',lb).onclick=hide;$('.pv',lb).onclick=()=>show(i-1);$('.nx',lb).onclick=()=>show(i+1);
    lb.addEventListener('click',e=>{if(e.target===lb)hide()});
    addEventListener('keydown',e=>{if(!lb.classList.contains('on'))return;if(e.key==='Escape')hide();if(e.key==='ArrowRight')show(i+1);if(e.key==='ArrowLeft')show(i-1)});}

  // live preview: scale a desktop-width iframe into the frame, load on click
  const vp=$('.live .vp');
  if(vp){const fr=$('iframe',vp),cover=$('.cover',vp);
    const fit=()=>{const w=vp.clientWidth;if(innerWidth<700){fr.style.width=w+'px';fr.style.height=vp.clientHeight+'px';fr.style.transform='none'}else{const s=w/1440;fr.style.width='1440px';fr.style.height=(vp.clientHeight/s)+'px';fr.style.transform=`scale(${s})`}};
    addEventListener('resize',fit);fit();
    $('button',cover).addEventListener('click',()=>{fr.src=fr.dataset.src;cover.classList.add('off')});}
})();
