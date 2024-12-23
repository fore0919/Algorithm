import java.util.Map;
import java.util.Set;
import java.util.function.BiFunction;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;

class Solution {

    // https://school.programmers.co.kr/learn/courses/30/lessons/181934

    public int solution(String ineq, String eq, int n, int m) {
        Map<String, BiFunction<Integer, Integer, Boolean>> functions = Map.of(
                ">=", (a, b) -> a >= b,
                "<=", (a, b) -> a <= b,
                ">!", (a, b) -> a > b,
                "<!", (a, b) -> a < b);
        return functions.get(ineq + eq).apply(n, m) ? 1 : 0;
    }

    // https://school.programmers.co.kr/learn/courses/30/lessons/181935

    public int solution(int n) {
        if (n % 2 == 0) {
            return IntStream.rangeClosed(1, n).filter(i -> i % 2 == 0).map(i -> (int) Math.pow(i, 2)).sum();
        } else {
            return IntStream.rangeClosed(1, n).filter(i -> i % 2 == 1).sum();
        }
    }

    // https://school.programmers.co.kr/learn/courses/30/lessons/181932

    public String solution(String code) {
        String answer = "";
        int mode = 0;
        for (int i = 0; i < code.length(); i++) {
            if (code.charAt(i) == '1')
                mode = 1 - mode;
            else if (i % 2 == mode)
                answer += code.charAt(i);
        }
        return "".equals(answer) ? "EMPTY" : answer;
    }

    // https://school.programmers.co.kr/learn/courses/30/lessons/181931

    public int solution(int a, int d, boolean[] included) {
        int answer = 0;
        for (int i = 0; i < included.length; i++) {
            if (included[i])
                answer += a + (d * i);
        }
        return answer;
    }

    public int solution_eazy(int a, int d, boolean[] included) {
        return IntStream.range(0, included.length).map(idx -> included[idx] ? a + (idx * d) : 0).sum();
    }

    // https://school.programmers.co.kr/learn/courses/30/lessons/181930

    public int solution(int a, int b, int c) {
        Set<Integer> arr = Stream.of(a, b, c).collect(Collectors.toSet());
        return (a + b + c) * (arr.size() < 3 ? a * a + b * b + c * c : 1)
                * (arr.size() < 2 ? a * a * a + b * b * b + c * c * c : 1);
    }

    // https://school.programmers.co.kr/learn/courses/30/lessons/181929

    public int solution(int[] num_list) {
        int sum = 0;
        int product = 1;
        for (int i = 0; i < num_list.length; i++) {
            sum += num_list[i];
            product *= num_list[i];
        }
        return product < sum * sum ? 1 : 0;
    }

    // https://school.programmers.co.kr/learn/courses/30/lessons/181928

    public int solution(int[] num_list) {
        String a = "";
        String b = "";
        for (int i = 0; i < num_list.length; i++) {
            if (num_list[i] % 2 == 0)
                a += Integer.toString(num_list[i]);
            else
                b += Integer.toString(num_list[i]);
        }
        return Integer.valueOf(a) + Integer.valueOf(b);
    }

    public int solution(int[] numList) {
        return Integer
                .parseInt(Arrays.stream(numList).filter(value -> value % 2 != 0).mapToObj(String::valueOf)
                        .collect(Collectors.joining()))
                + Integer.parseInt(Arrays.stream(numList).filter(value -> value % 2 == 0).mapToObj(String::valueOf)
                        .collect(Collectors.joining()));
    }

    // https://school.programmers.co.kr/learn/courses/30/lessons/181927

    public int[] solution(int[] num_list) {
        int len = num_list.length;
        int[] answer = Arrays.copyOf(num_list, len + 1);
        int a = num_list[len - 1];
        int b = num_list[len - 2];
        answer[answer.length - 1] = a > b ? a - b : a * 2;
        return answer;
    }

    // https://school.programmers.co.kr/learn/courses/30/lessons/181926

    public int solution(int n, String control) {
        int answer = 0;
        for (int i = 0; i < control.length(); i++) {
            if (control.charAt(i) == 'w')
                answer += 1;
            else if (control.charAt(i) == 's')
                answer -= 1;
            else if (control.charAt(i) == 'd')
                answer += 10;
            else
                answer -= 10;
        }
        return answer + n;
    }

    // with switch

    public int solution(int n, String control) {
        int answer = n;
        for (char ch : control.toCharArray()) {
            switch (ch) {
                case 'w':
                    answer += 1;
                    break;
                case 's':
                    answer -= 1;
                    break;
                case 'd':
                    answer += 10;
                    break;
                case 'a':
                    answer -= 10;
                    break;
                default:
                    break;
            }
        }
        return answer;
    }

    // https://school.programmers.co.kr/learn/courses/30/lessons/181925

    public String solution(int[] numLog) {
        String answer = "";
        for (int i = 1; i < numLog.length; i++) {
            int num = numLog[i] - numLog[i - 1];
            switch (num) {
                case 1:
                    answer += "w";
                    break;
                case -1:
                    answer += "s";
                    break;
                case 10:
                    answer += "d";
                    break;
                case -10:
                    answer += "a";
                    break;
                default:
                    break;
            }
        }
        return answer;
    }

    // https://school.programmers.co.kr/learn/courses/30/lessons/181924

    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = Arrays.copyOf(arr, arr.length);
        for (int[] query : queries) {
            int i = query[0];
            int j = query[1];
            int x = answer[i];
            answer[i] = answer[j];
            answer[j] = x;
        }
        return answer;
    }

    // https://school.programmers.co.kr/learn/courses/30/lessons/181923

    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = new int[queries.length];
        Arrays.fill(answer, -1);
        for (int i = 0; i < queries.length; i++) {
            int s = queries[i][0], e = queries[i][1], k = queries[i][2];
            for (int j = s; j <= e; j++) {
                if (k < arr[j]) {
                    answer[i] = answer[i] == -1 ? arr[j] : Math.min(answer[i], arr[j]);
                }
            }
        }
        return answer;
    }

    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = {};
        return IntStream.range(0, queries.length)
                .map(q -> IntStream.rangeClosed(queries[q][0], queries[q][1])
                        .map(i -> arr[i])
                        .filter(i -> i > queries[q][2])
                        .min().orElse(-1))
                .toArray();
    }

    public int[] solution(int[] arr, int[][] queries) {
        for (int i = 0; i < queries.length; i++) {
            int s = queries[i][0], e = queries[i][1], k = queries[i][2];
            for (int j = s; j <= e; j++) {
                if (j % k == 0) {
                    arr[j]++;
                }
            }
        }
        return arr;
    }

    // https://school.programmers.co.kr/learn/courses/30/lessons/181921?
    public int[] solution(int l, int r) {
        List<Integer> arr = new ArrayList<>();
        for (int i = l; i <= r; i++) {
            String str = "" + i;
            int cnt = 0;
            for (int j = 0; j < str.length(); j++) {
                if (str.charAt(j) == '5' | str.charAt(j) == '0')
                    cnt += 1;
            }

            if (cnt == str.length()) {
                arr.add(i);
            }
        }
        int[] answer = arr.stream().mapToInt(i -> i).toArray();
        int[] empty = { -1 };
        if (answer.length == 0)
            return empty;
        return answer;
    }

}
