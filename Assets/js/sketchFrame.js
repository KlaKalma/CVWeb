/**
 * Live p5.js sketches in the portfolio pages.
 * The sketch only loads when the visitor clicks the button, then the frame is scaled to the page width
 * (the sketch keeps its original size, so the mouse clicks still land in the right place).
 */
document.querySelectorAll('.sketch-frame').forEach(function (box) {
  var width = Number(box.dataset.width);
  var height = Number(box.dataset.height);

  function fit() {
    var scale = box.clientWidth / width;
    box.style.height = (height * scale) + 'px';
    var frame = box.querySelector('iframe');
    if (frame) frame.style.transform = 'scale(' + scale + ')';
  }

  box.querySelector('button').addEventListener('click', function () {
    var frame = document.createElement('iframe');
    frame.src = box.dataset.src;
    frame.width = width;
    frame.height = height;
    frame.title = 'Live simulation';
    box.innerHTML = '';
    box.appendChild(frame);
    fit();
    frame.focus();
  });

  window.addEventListener('resize', fit);
  fit();
});
