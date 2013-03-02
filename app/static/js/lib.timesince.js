// Port of django's timesince
var chunks = [
  [60 * 60 * 24 * 365, 'year'],
  [60 * 60 * 24 * 30, 'month'],
  [60 * 60 * 24 * 7, 'week'],
  [60 * 60 * 24, 'day'],
  [60 * 60, 'hour'],
  [60, 'minute']
];

Date.prototype.time_since = function() {
  var delta = Math.floor((Date.now() - this.getTime()) / 1000);
  if (delta <= 0) {
    return '0 minutes ago';
  }
  var last, count;
  chunks.some(function(chunk, i){
    count = Math.floor(delta / chunk[0]);
    last = i;
    return count != 0;
  });
  var str = count + ' ' + (count == 1 ? chunks[last][1] : chunks[last][1] + 's');

  if (last + 1 < chunks.length) {
    var chunk = chunks[last + 1];
    var second = Math.round((delta - (chunks[last][0] * count)) / chunk[0]);
    if (second != 0)
      str += ', ' + second + ' ' + (second == 1 ? chunk[1] : chunk[1] + 's');
  }

  return str + ' ago';
};
