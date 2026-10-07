/**
 * Live p5.js sketches in the portfolio pages.
 * The sketch starts right after the page has loaded (so it does not delay the page animations),
 * and its frame is scaled to the page width
 * (the sketch keeps its original size, so the mouse clicks still land in the right place).
 */
document.querySelectorAll('.sketch-frame').forEach(function (box) {
  var width = Number(box.dataset.width);
  var height = Number(box.dataset.height);
  var frame = null;

  function fit() {
    var scale = box.clientWidth / width;
    box.style.height = (height * scale) + 'px';
    if (frame) frame.style.transform = 'scale(' + scale + ')';
  }

  function start() {
    frame = document.createElement('iframe');
    frame.src = box.dataset.src;
    frame.width = width;
    frame.height = height;
    frame.title = 'Live simulation';
    box.appendChild(frame);
    fit();
  }

  window.addEventListener('resize', fit);
  fit();
  if (document.readyState === 'complete') start();
  else window.addEventListener('load', start);
});
