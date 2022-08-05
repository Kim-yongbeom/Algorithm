function solution(numbers) {
  var answer = [];
  var sum = [];

  for (var i = 0; i < numbers.length; i++) {
    for (var j = i + 1; j < numbers.length; j++) {
      sum.push(numbers[i] + numbers[j]);
    }
  }

  sum = [...new Set(sum)];

  console.log(sum);

  sum.sort((a, b) => {
    return a - b;
  });

  return sum;
}
