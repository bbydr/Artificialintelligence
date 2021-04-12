
% EARIN Introduction to Artificial Intelligence - Exercise 3b
% Merve Rana Kýzýl
% Beste Baydur

is_triple(A, B, C) :-
  D is C*C - A*A - B*B,  % must use "is" for arithmetic
  D = 0.

solve_triple(A, B, C) :-
    between(1, 20, A),
    between(1, 20, B),
    A < B,
    between(1, 20, C),
    B < C,
    is_triple(A, B, C).
