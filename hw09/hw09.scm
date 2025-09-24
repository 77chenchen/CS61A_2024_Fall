(define (curry-cook formals body)
        (let ((arg (car formals)))
        (if (null? (cdr formals))
            `(lambda (,arg) ,body)
            `(lambda (,arg) ,(curry-cook (cdr formals) body))
        )
        )

)

(define (curry-consume curry args)
  'YOUR-CODE-HERE)

(define-macro (switch expr options)
  (switch-to-cond (list 'switch expr options)))

(define (switch-to-cond switch-expr)
  (cons _________
        (map (lambda (option)
               (cons _______________ (cdr option)))
             (car (cdr (cdr switch-expr))))))
