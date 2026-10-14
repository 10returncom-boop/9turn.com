/* ==========================================================================
   9Turn 九回錦 | v2 共用互動腳本
   涵蓋：行動版導覽 / MegaMenu / 全站搜尋(autocomplete) / TOC 自動生成
        / 收藏本頁 / 浮動導航 / 章節捲動標記 / 年份
   ========================================================================== */
(function(){
  'use strict';

  /* ---------- 行動版導覽開關 ---------- */
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.site-nav');
  if(toggle && nav){
    toggle.addEventListener('click', function(){
      nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', nav.classList.contains('open') ? 'true' : 'false');
    });
    nav.querySelectorAll('a,summary').forEach(function(a){
      a.addEventListener('click', function(){ nav.classList.remove('open'); });
    });
  }

  /* ---------- 頁尾年份 ---------- */
  var y = document.getElementById('year');
  if(y){ y.textContent = new Date().getFullYear(); }

  /* ---------- TOC 文章目錄：從 .article 的 H2/H3 自動生成 ---------- */
  var tocBox = document.querySelector('.toc[data-toc]');
  var article = document.querySelector('.article');
  if(tocBox && article){
    var heads = article.querySelectorAll('h2, h3');
    var tocList = tocBox.querySelector('ol');
    if(heads.length && tocList){
      heads.forEach(function(h, i){
        if(!h.id){ h.id = 'sec-' + i; }
        var li = document.createElement('li');
        var a = document.createElement('a');
        a.href = '#' + h.id;
        a.textContent = h.textContent;
        if(h.tagName === 'H3'){ a.className = 'lvl-3'; }
        li.appendChild(a);
        tocList.appendChild(li);
      });
      /* 捲動標記目前章節 */
      var links = tocList.querySelectorAll('a');
      var onScroll = function(){
        var pos = window.scrollY + 110;
        var current = null;
        links.forEach(function(l){
          var t = document.getElementById(l.getAttribute('href').slice(1));
          if(t && t.offsetTop <= pos){ current = l; }
        });
        links.forEach(function(l){ l.classList.remove('active'); });
        if(current){ current.classList.add('active'); }
      };
      window.addEventListener('scroll', onScroll, {passive:true});
      onScroll();
    }
  }

  /* ---------- 全站搜尋：autocomplete + 多面向 Tag 篩選 ---------- */
  var index = window.SITE_INDEX || [];
  var sToggle = document.querySelector('[data-toggle-search]');
  var overlay = document.querySelector('.search-overlay');
  var input = document.getElementById('site-search');
  var suggest = document.querySelector('.search-suggest');
  var activeFacet = '';
  if(sToggle && overlay && input && suggest){
    var close = function(){ overlay.hidden = true; overlay.setAttribute('aria-hidden','true'); };
    sToggle.addEventListener('click', function(){
      overlay.hidden = false; overlay.setAttribute('aria-hidden','false');
      setTimeout(function(){ input.focus(); }, 30);
    });
    overlay.addEventListener('click', function(e){ if(e.target === overlay){ close(); } });
    document.addEventListener('keydown', function(e){
      if(e.key === 'Escape'){ close(); }
    });
    var render = function(){
      var q = input.value.trim().toLowerCase();
      var out = '';
      var n = 0;
      index.forEach(function(r){
        if(n >= 14){ return; }
        var title = r[0], url = r[1], tag = r[2];
        if(activeFacet && tag !== activeFacet){ return; }
        if(q){
          var hitTitle = title.toLowerCase().indexOf(q) >= 0;
          var hitTag = tag.toLowerCase().indexOf(q) >= 0;
          if(!hitTitle && !hitTag){ return; }
        }
        var shown = title;
        if(q && title.toLowerCase().indexOf(q) >= 0){
          var i = title.toLowerCase().indexOf(q);
          shown = title.slice(0,i) + '<span class="hl">' + title.slice(i, i+q.length) + '</span>' + title.slice(i+q.length);
        }
        out += '<a href="' + url + '"><span>' + shown + '</span>' + (tag ? '<span class="sc-tag">' + tag + '</span>' : '') + '</a>';
        n++;
      });
      if(!out){
        out = '<a href="#"><span>沒有符合「' + input.value + '」的結果，試試「資產」「名錶」「配置」</span></a>';
      }
      suggest.innerHTML = out;
    };
    input.addEventListener('input', render);
    render();
    /* 多面向篩選：點結果 tag 精煉 */
    suggest.addEventListener('click', function(e){
      var a = e.target.closest('a');
      if(a && a.getAttribute('href') === '#'){ e.preventDefault(); }
    });
  }

  /* ---------- 收藏本頁（localStorage） ---------- */
  var saveBtn = document.querySelector('[data-save]');
  if(saveBtn){
    var key = '9t-saves';
    var url = location.pathname.split('/').pop() || 'index.html';
    var getSaves = function(){ try{ return JSON.parse(localStorage.getItem(key)||'[]'); }catch(e){ return []; } };
    var isSaved = function(){ return getSaves().indexOf(url) >= 0; };
    var paint = function(){
      saveBtn.classList.toggle('saved', isSaved());
      saveBtn.setAttribute('aria-pressed', isSaved() ? 'true' : 'false');
      saveBtn.querySelector('span').textContent = isSaved() ? '已收藏' : '收藏本頁';
    };
    saveBtn.addEventListener('click', function(){
      var s = getSaves();
      if(s.indexOf(url) >= 0){ s = s.filter(function(x){ return x !== url; }); }
      else{ s.push(url); }
      try{ localStorage.setItem(key, JSON.stringify(s)); }catch(e){}
      paint();
    });
    paint();
  }

  /* ---------- 浮動導航：捲動後顯示，回上頁 / 回首頁 ---------- */
  var fBack = document.querySelector('.f-back');
  var fHome = document.querySelector('.f-home');
  var fnav = document.querySelector('.float-nav');
  if(fBack){
    fBack.addEventListener('click', function(e){
      if(history.length > 1){ e.preventDefault(); history.back(); }
      else{ e.preventDefault(); window.location.href = 'index.html'; }
    });
  }
  if(fnav){
    var showF = function(){ fnav.classList.add('show'); };
    var hideF = function(){ fnav.classList.remove('show'); };
    if(window.scrollY > 260){ showF(); }
    window.addEventListener('scroll', function(){
      window.scrollY > 260 ? showF() : hideF();
    }, {passive:true});
  }

  /* ---------- 章節側欄：捲動標記目前章節（optional） ---------- */
  var navLinks = document.querySelectorAll('.sidebar a[data-target]');
  if(navLinks.length){
    var targets = [];
    navLinks.forEach(function(l){
      var id = l.getAttribute('data-target');
      if(id){ targets.push({link:l, el:document.getElementById(id)}); }
    });
    var onScroll2 = function(){
      var pos = window.scrollY + 90;
      var current = null;
      targets.forEach(function(t){ if(t.el && t.el.offsetTop <= pos){ current = t.link; } });
      targets.forEach(function(t){ if(t.link.classList.contains('active')){ t.link.classList.remove('active'); } });
      if(current){ current.classList.add('active'); }
    };
    if(targets.length){ window.addEventListener('scroll', onScroll2, {passive:true}); onScroll2(); }
  }
})();
