;(function(){
  function id(v){return document.getElementById(v); }
  function loadbar() {
    var ovrl = id("overlay"),
        prog = id("progress"),
        stat = id("progstat"),
        img = document.images,
        c = 0;
        tot = img.length;

    function imgLoaded(){
      c += 1;
      var perc = ((100/tot*c) << 0) +"%";
      prog.style.width = perc;
      if (perc < 20)
      {
        stat.innerHTML = "Loading your cart";
      }
      else if (perc <40 && perc > 20) 
      {
        stat.innerHTML = "Loading your memories";
      }
      else if(perc > 40 && perc <60)
      {
        stat.innerHTML = "Loading "+ perc;
      }
      else if(perc > 60 && perc < 80)
      {
        stat.innerHTML = "Loading "+ perc;
      }
      else  
      {
        stat.innerHTML = "Loading "+ perc;
      }

      if(c===tot) return doneLoading();
    }
    function doneLoading(){
      ovrl.style.opacity = 0;
      setTimeout(function(){ 
        ovrl.style.display = "none";
      }, 1200);
    }
    for(var i=0; i<tot; i++) {
      var tImg     = new Image();
      tImg.onload  = imgLoaded;
      tImg.onerror = imgLoaded;
      tImg.src     = img[i].src;
    }    
  }
  document.addEventListener('DOMContentLoaded', loadbar, false);
}());