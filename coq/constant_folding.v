(**This is based on MTG *)

(**The syntax of formula*)
(** bb1: 
*   bb2: (1*2)
*   bb3: (2*3)  
*   bb4: (1*2)
*   bb5: (1*5)
*   bb6: (5*6)
*   bb7: (1*5) *)

Inductive formula : Type :=
| T      :   nat -> formula
| TaskCD    :   formula -> formula -> formula    
| TaskDD    :   formula -> formula -> formula
| TaskAnd   :   formula -> formula -> formula
| TaskOr    :   formula -> formula -> formula.


Infix "*"   :=  TaskCD.
Infix "-"   :=  TaskDD.
Infix "||"  :=  TaskOr.
Infix "&&"  :=  TaskAnd.

Check (T 1) * (T 2).
Check (T 1) - (T 2).
Check (T 1 * T 2) || (T 3 * T 4).
Check (T 3) || (T 6) || ((T 2) * (T 4 )).
Check T 1.

(**The syntax of formula/EEC*)
Inductive formula : Type :=
| Task      :   nat -> formula
| TaskCD    :   formula -> formula -> formula    
| TaskDD    :   formula -> formula -> formula
| TaskAnd   :   formula -> formula -> formula
| TaskOr    :   formula -> formula -> formula.

    


(**The syntax of block*)
Inductive block : Type :=
  | Block: mtg -> block
  | BB : formula -> block.

(**The syntax of MTG*)
Definition mtg (b : block)(l: list block) :=
    match l with 
    | [] => block
    | x :: _ => x
    end.

(**The syntax of ordering*)
(**Under construction...*)

(**The function which is used to get the task_ordering by analyzing the MTG*)
Fixpoint mtg_eval (g : mtg) : task_ordering :=
    match g with
    end.

(**The definition which is used to set what kind of behavior should be seen as correct*)
Definition mtg_equiv(g1 g2 : mtg) : Prop :=
    forall (odering : task_ordering),
    mtg_eval odering g1 = mtg_eval ordering g2.


(**The definition which is used to set the soundness of the general transformation of MTG*)
Definition gtrans_sound (gtrans : mtg -> mtg) : Prop :=
    forall (g : mtg),
    mtg_equiv g (gtrans g).


(**The function which is used to merge the mtg from different hierachy layer*)
Fixpoint mtg_transformation (g : mtg) : mtg :=
    match g with
    end.

(**The theorem which is used to prove the soundness of the mtg_transformation*)
Theorem mtg_transformation_sound :
    gtrans_sound mtg_transformation.





(**Following is from the constant propogation *)
Inductive aexp : Type :=
  | ANum : nat -> aexp
  | APlus : aexp -> aexp -> aexp
  | AMinus : aexp -> aexp -> aexp
  | AMult : aexp -> aexp -> aexp.

Fixpoint aeval (a : aexp) : nat := match a with
  | ANum n => n
  | APlus a1 a2 => (aeval a1) + (aeval a2)
  | AMinus a1 a2  => (aeval a1) - (aeval a2)
  | AMult a1 a2 => (aeval a1) * (aeval a2)
  end.

Definition aequiv (a1 a2 : aexp) : Prop :=
      ∀ (st:state),
          aeval st a1 = aeval st a2.


Definition atrans_sound (atrans : aexp → aexp) : Prop :=
      ∀ (a : aexp),
          aequiv a (atrans a).


Fixpoint fold_constants_aexp (a : aexp) : aexp :=
  match a with
  | ANum n ⇒ ANum n
  | AId i ⇒ AId i
  | APlus a1 a2 ⇒
    match (fold_constants_aexp a1, fold_constants_aexp a2)
    with
    | (ANum n1, ANum n2) ⇒ ANum (n1 + n2)
    | (a1', a2') ⇒ APlus a1' a2'
    end
  | AMinus a1 a2 ⇒
    match (fold_constants_aexp a1, fold_constants_aexp a2)
    with
    | (ANum n1, ANum n2) ⇒ ANum (n1 - n2)
    | (a1', a2') ⇒ AMinus a1' a2'
    end
  | AMult a1 a2 ⇒
    match (fold_constants_aexp a1, fold_constants_aexp a2)
    with
    | (ANum n1, ANum n2) ⇒ ANum (n1 * n2)
    | (a1', a2') ⇒ AMult a1' a2'
    end
  end.

Fixpoint fold_constants_bexp (b : bexp) : bexp:=
    match b with
    end.

Fixpoint fold_constants_cexp (c : cexp) : cexp:=
    match c with
    end.

(** Following theorem prove the correctness of the "fold_constants_aexp" *)
Theorem fold_constants_aexp_sound :
      atrans_sound fold_constants_aexp.

