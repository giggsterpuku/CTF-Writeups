;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; Write-Up ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Challenge:
; Category: Reverse Engineering
; Description: What integer does this program print with argument 2541039191? File: chall_3.S Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})
; Hints:
;	-1: Beep boop beep boop...
;
; The annotations in this file are basically going to be the walkthrough/write-up of the chall, showing the correct thought process to take in
; solving it.
;
; Flag: picoCTF{00000039}
; Solved by giggsterpuku in picoGym
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


	.arch armv8-a
	.file	"chall_3.c"
	.text
	.align	2
	.global	func1
	.type	func1, %function
func1: ; basically returns the number of 1's in the binary representation of the input
	stp	x29, x30, [sp, -48]!
	add	x29, sp, 0
	str	w0, [x29, 28] ; stack --> [x29 + 28] |2541039191|
	str	wzr, [x29, 44] ;          [x29 + 44] |     0    |
	b	.L2 ; go to .L2
.L4:
	ldr	w0, [x29, 28]
	and	w0, w0, 1 ; w0 = 0 if the val is even, 1 if val is odd (every odd number ends in 1 in binary, even ends in 0)
	cmp	w0, 0 ; if even, just get straight to .L3
	beq	.L3
	ldr	w0, [x29, 44]
	bl	func2 ; if odd, branch to func2
	str	w0, [x29, 44]
.L3:
	ldr	w0, [x29, 28]
	lsr	w0, w0, 1 ; right shift on value in [x29 + 28], but 0 bit replaces val that would have be placed from the end of the binary representation of the number to the front
	str	w0, [x29, 28]
.L2:
	ldr	w0, [x29, 28] ; load current val in [x29 + 28] into register
	cmp	w0, 0 ; while that current val is not zero, run the loop from .L4 to these cmp and bne instructions
	bne	.L4
	ldr	w0, [x29, 44]
	ldp	x29, x30, [sp], 48
	ret
	.size	func1, .-func1
	.align	2
	.global	func2
	.type	func2, %function
func2: ; basically adds 3 to value in [x29 + 44]
	sub	sp, sp, #16
	str	w0, [sp, 12]
	ldr	w0, [sp, 12]
	add	w0, w0, 3
	add	sp, sp, 16
	ret
	.size	func2, .-func2
	.section	.rodata
	.align	3
.LC0:
	.string	"Result: %ld\n"
	.text
	.align	2
	.global	main
	.type	main, %function
main:
	stp	x29, x30, [sp, -48]!
	add	x29, sp, 0
	str	w0, [x29, 28] ; input here (2541039191)
	str	x1, [x29, 16]
	ldr	x0, [x29, 16]
	add	x0, x0, 8
	ldr	x0, [x0]
	bl	atoi
	bl	func1
	str	w0, [x29, 44]
	adrp	x0, .LC0
	add	x0, x0, :lo12:.LC0
	ldr	w1, [x29, 44] ; prints out what is in [x29 + 44]
	bl	printf
	nop
	ldp	x29, x30, [sp], 48
	ret
	.size	main, .-main
	.ident	"GCC: (Ubuntu/Linaro 7.5.0-3ubuntu1~18.04) 7.5.0"
	.section	.note.GNU-stack,"",@progbits

; Key: 2541039191 = 0b10010111011101010010111001010111, there are 19 1's in the binary representation, 19 * 13 = 57 *ANSWER*
