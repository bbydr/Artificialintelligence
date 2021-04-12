
% EARIN Introduction to Artificial Intelligence - Exercise 3c
% Merve Rana Kýzýl
% Beste Baydur

is_triple(A, B, C) :-
  D is C*C - A*A - B*B,
  D = 0.

solve_triple2(A, B, C, T) :-
  N is 1000,
  between(1,N, A),
  between(A, N, B),
  C is N - A - B,
  statistics(cputime,V),
  ( V < T
     -> is_triple(A, B, C)
     ; abort()
  ).

