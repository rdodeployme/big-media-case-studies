/* Big Digital work site: motion and interactions. Everything degrades to a static page. */
(function(){
  const $=(s,r=document)=>r.querySelector(s), $$=(s,r=document)=>[...r.querySelectorAll(s)];
  const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;

  // header, scroll progress, sticky audit button, hero tilt, case sub-nav handover
  const top=$('.top'), prog=$('.prog'), tilt=$('.tilt'), sticky=$('.sticky'), sub=$('.subnav'), contact=$('#contact');
  function onScroll(){
    const y=scrollY, h=document.documentElement.scrollHeight-innerHeight;
    top&&top.classList.toggle('solid',y>40);
    prog&&(prog.style.width=(h>0?y/h*100:0)+'%');
    if(sticky){let show=y>innerHeight*.7;if(contact){const r=contact.getBoundingClientRect();if(r.top<innerHeight&&r.bottom>0)show=false}sticky.classList.toggle('on',show)}
    if(sub){document.body.classList.toggle('sub-on',sub.getBoundingClientRect().top<=1)}
    if(tilt&&!reduce){const r=tilt.getBoundingClientRect(), p=Math.min(1,Math.max(0,(innerHeight-r.top)/(innerHeight*0.9)));
      tilt.style.transform=`rotateX(${14*(1-p)}deg) scale(${0.94+0.06*p})`;}
  }
  addEventListener('scroll',onScroll,{passive:true}); onScroll();

  // reveal + count-up (supports decimals via data-d and a suffix via data-s)
  const count=el=>{const end=parseFloat(el.dataset.n);if(isNaN(end)||reduce)return;
    const dec=parseInt(el.dataset.d||'0',10), suf=el.dataset.s||'', dur=1400, t0=performance.now();
    const fmt=v=>(dec?v.toFixed(dec):Math.round(v).toLocaleString('en-AU'))+suf;
    const f=t=>{const p=Math.min(1,(t-t0)/dur),v=end*(1-Math.pow(1-p,3));el.textContent=fmt(v);if(p<1)requestAnimationFrame(f)};
    el.textContent=fmt(0);requestAnimationFrame(f)};
  const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');$$('[data-n]',e.target).forEach(count);if(e.target.dataset.n!==undefined)count(e.target);io.unobserve(e.target)}}),{rootMargin:'0px 0px -8% 0px'});
  $$('.rv,.countme').forEach(el=>io.observe(el));

  // sub-nav active section
  const links=$$('.subnav a[href^="#"]');
  if(links.length){const so=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){links.forEach(a=>a.classList.toggle('on',a.getAttribute('href')==='#'+e.target.id))}}),{rootMargin:'-45% 0px -50% 0px'});
    links.forEach(a=>{const t=$(a.getAttribute('href'));t&&so.observe(t)})}

  // work filters
  $$('.filters .chip').forEach(c=>c.addEventListener('click',()=>{$$('.filters .chip').forEach(b=>b.setAttribute('aria-pressed',b===c));
    const f=c.dataset.f;$$('.card').forEach(r=>r.classList.toggle('hide',f!=='all'&&!r.dataset.f.includes(f)))}));

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
    shots.forEach((s,k)=>{s.addEventListener('click',()=>show(k));s.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();show(k)}})});
    $('.x',lb).onclick=hide;$('.pv',lb).onclick=()=>show(i-1);$('.nx',lb).onclick=()=>show(i+1);
    lb.addEventListener('click',e=>{if(e.target===lb)hide()});
    addEventListener('keydown',e=>{if(!lb.classList.contains('on'))return;if(e.key==='Escape')hide();if(e.key==='ArrowRight')show(i+1);if(e.key==='ArrowLeft')show(i-1)});}

  // live preview: scale a desktop-width iframe into the frame, load on click
  const vp=$('.live .vp');
  if(vp){const fr=$('iframe',vp),cover=$('.cover',vp);
    const fit=()=>{const w=vp.clientWidth;if(innerWidth<700){fr.style.width=w+'px';fr.style.height=vp.clientHeight+'px';fr.style.transform='none'}else{const s=w/1440;fr.style.width='1440px';fr.style.height=(vp.clientHeight/s)+'px';fr.style.transform=`scale(${s})`}};
    addEventListener('resize',fit);fit();
    $('button',cover).addEventListener('click',()=>{fr.src=fr.dataset.src;cover.classList.add('off')});}

  // audit form: no backend, so it hands a filled-in email to the visitor's mail app
  const form=$('#audit-form');
  if(form){const err=$('.err',form);
    form.addEventListener('submit',ev=>{ev.preventDefault();
      const v=n=>(form.elements[n]&&form.elements[n].value||'').trim();
      const missing=[];if(!v('name'))missing.push('your name');
      if(!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v('email')))missing.push('a valid email');
      const rq=form.dataset.req||'message';if(!v(rq))missing.push(rq==='website'?'your website':'what’s slowing you down');
      if(missing.length){err.style.color='';err.textContent='Please add '+missing.join(', ')+'.';const first=form.querySelector(!v('name')?'#f-name':!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v('email'))?'#f-email':rq==='website'?'#f-site':'#f-msg');first&&first.focus();return}
      err.textContent='';
      const needs=$$('input[name=need]:checked',form).map(c=>c.value).join(', ')||'Not sure yet';
      const lines=['Hi Big Digital,','','I’d like a free website and ads audit.','',
        'Name: '+v('name'),'Business: '+(v('business')||'-'),'Email: '+v('email'),'Mobile: '+(v('phone')||'-'),'Website: '+(v('website')||'-'),'Help with: '+needs,'',
        'What’s slowing us down:',v('message')||'-','','Sent from the Big Digital work site.'];
      const subject='Free audit request: '+(v('business')||v('name'));
      location.href='mailto:'+form.dataset.to+'?subject='+encodeURIComponent(subject)+'&body='+encodeURIComponent(lines.join('\n'));
      err.style.color='var(--lime)';err.textContent='Your email app should now be open with the request ready to send.';
    });}
})();
