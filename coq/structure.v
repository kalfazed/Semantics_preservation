Section Structure.

(**Type of x, x*y, x-y**)
Inductive base : Type :=
| nil_Task      :       base
| Task          :       nat -> base 
| TaskCD        :       nat -> nat -> base 
| TaskCDD       :       nat -> nat -> base.

(**Type of (), (x), (x y)**)
Inductive disjunction : Type :=
| nil_disj      :       disjunction 
| cons_disj     :       base -> disjunction -> disjunction.

(**Type of ()(), (x)(y), (x y)(z)**)
Inductive conjunction : Type :=
| nil_conj      :       conjunction
| cons_conj     :       disjunction -> conjunction -> conjunction.

(**Type of <x: y>, <x: y-z>, <x: (y)(z w)>**)
Inductive EEC : Type :=
| eec           :       nat -> conjunction -> EEC.

(**Type of [<x:y> <x:(y z)> <x:(y)(z w)>]**)
Inductive mtg : Type :=
| nil_mtg       :       mtg 
| cons_mtg      :       EEC -> mtg -> mtg.

(**Type of {[mtg1] [mtg2] ... [mtgN]}**)
Inductive mtgList : Type :=
| nil_mtgList   :       mtgList 
| cons_mtgList  :       mtg -> mtgList -> mtgList.

Inductive base_list : Type :=
| nil_base      :       base_list 
| cons_base     :       nat -> base_list -> base_list.


(**Next step, I need to create the mathmatic synbolic to each expression**)
(**May be I should use implicit arguments**)
Notation "( # x )" := (Task x).
Notation "( x ** y )" := (TaskCD x y).
Notation "( x -- y )" := (TaskCDD x y).

Notation "()" := nil_Task.
Notation "x :: y" := (cons_disj x y)
                     (at level 60, right associativity).
                
Notation "[ x , .. , y ]" := (cons_disj  x .. (cons_disj y nil_disj) ..)
                     (at level 60, right associativity).
Notation "{ x ; .. ; y }" := (cons_conj  x .. (cons_conj y nil_conj) ..)
                     (at level 65, right associativity).

(**(1*2 2*3)**)
(**(1 2)**)
Check [(),()].
Check [(1**2), (2--3)].
Check [(#1), (#2)].
Check [(#1)].
Check {[(), ()]}.
Check {[(), ()] ;
        [(#1), (#2)] ;
        [(#1), (#2)]}.
Definition test := 
        EEC 1 {[()]} |
        EEC 2 {[(1--2)]} |
        EEC 3 {[(1--3)]} |
        EEC 4 {[(#2), (1**3)]} |
        EEC 5 {[(#3), (1**2))]; [(#4)]}.

Notation "[ x \/ y ]" := (cons_disj x y).


Check {1 ** 2}.
Check {1 -- 2}.

End Structure.
