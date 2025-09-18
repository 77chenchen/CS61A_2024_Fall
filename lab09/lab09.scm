(define (over-or-under num1 num2)
        (cond((< num1 num2) -1)
             ((> num1 num2) 1)
             ((= num1 num2) 0))
)

(define (make-adder num) 
        (lambda (inc) (+ inc num))
)

(define (composed f g) 
        (lambda (x) (f(g x)))
)

(define (repeat f n)
        (if (= 1 n)
                (lambda (x) (f x))
                (lambda (x) ((repeat f (- n 1)) (f x)))
        )
)
(define (max a b)
  (if (> a b)
      a
      b))

(define (min a b)
  (if (> a b)
      b
      a))

(define (gcd a b) 
        (cond ((= b 0) a)
                (else (gcd b (modulo a b))))



)
