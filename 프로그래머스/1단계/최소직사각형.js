function solution(sizes) {
  var maxSize = [0, 0];
  var size = sizes.map(([w, h]) => (w > h ? [w, h] : [h, w]));

  size.forEach(([w, h]) => {
    if (w > maxSize[0]) {
      maxSize[0] = w;
    }
    if (h > maxSize[1]) {
      maxSize[1] = h;
    }
  });

  return maxSize[0] * maxSize[1];
}
