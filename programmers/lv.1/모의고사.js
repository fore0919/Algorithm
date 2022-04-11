let answers = [1, 3, 2, 4, 2, 1, 3, 2, 4, 2, 1, 3, 2, 4, 2, 1, 3, 2, 4, 2];

function solution(answers) {

   let answer = [];

    const man1 = [1, 2, 3, 4, 5];
    const man2 = [2, 1, 2, 3, 2, 4, 2, 5];
    const man3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];

    let score = [0, 0, 0];

    for (let i = 0; i < answers.length; i++) {
        if (answers[i] === man1[i % man1.length]) score[0]++;
        if (answers[i] === man2[i % man2.length]) score[1]++;
        if (answers[i] === man3[i % man3.length]) score[2]++;
    }

    const max = Math.max(...score);

    for (let i = 0; i < score.length; i++) {
        if (max === score[i]) answer.push(i + 1);
    }

    return answer;
}

console.log(solution(answers));