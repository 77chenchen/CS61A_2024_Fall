(define-macro (trace expr) 
    (define operator (car expr))
    `(begin
        (define original ,operator)
        (define ,operator (lambda (n) 
                                (print (list(quote ,operator) n))
                                (original n)))
        (define result ,expr)
        (define ,operator original)
        result)
    
)