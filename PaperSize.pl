
% EARIN Introduction to Artificial Intelligence - Exercise 3a
% Merve Rana Kýzýl
% Beste Baydur

isGreaterOrEqual(X,Y) :-
    (  X =< Y
       -> true
       ;  false
    ).


isA0(A0, A1, A2, A3, A4, A5) :-
    isGreaterOrEqual(32, 32*A0 + 16*A1 + 8*A2 + 4*A3 + 2*A4 + A5).
