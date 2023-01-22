;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; Write-Up ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Challenge: ARMssembly 2
; Category: Reverse Engineering
; Description: What integer does this program print with argument 4189673334? File: chall_2.S Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})
; Hints:
;	-1: Loops
;
; The write-up is basically all the annotations I put here.
;
; Flag: picoCTF{ed2c0662}
; Points: 90
; Solved in picoGym
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

	.arch armv8-a
	.file	"chall_2.c"
	.text
	.align	2
	.global	func1
	.type	func1, %function
func1:	; gist your input * 3, so if our input is 4189673334...
	sub	sp, sp, #32
	str	w0, [sp, 12] ; your input stored in stack addr [sp + 12]
	str	wzr, [sp, 24] ; wzr val always zero if accessed, [sp + 24] = 0
	str	wzr, [sp, 28] ; [sp + 28] = 0
	b	.L2 ; jump to .L2
.L3:
	ldr	w0, [sp, 24]
	add	w0, w0, 3 ; adds three to [sp + 24]
	str	w0, [sp, 24]
	ldr	w0, [sp, 28]
	add	w0, w0, 1 ; [sp + 28] is like a loop counter
	str	w0, [sp, 28] ; goes back into .L2 from here
.L2:
	ldr	w1, [sp, 28] ; w1 = [sp + 28]
	ldr	w0, [sp, 12] ; w0 = [sp + 12], your input
	cmp	w1, w0
	bcc	.L3 ; if w1 >= w0 (your input) jump to .L3, basically repeats <your input> amount of times
	ldr	w0, [sp, 24] ; returns what's in [sp + 24], 4189673334 * 3 = 12569020002, in hex is 0x2ed2c0662
	add	sp, sp, 32
	ret
	.size	func1, .-func1
	.section	.rodata
	.align	3
.LC0:
	.string	"Result: %ld\n"
	.text
	.align	2
	.global	main
	.type	main, %function
main:
	stp	x29, x30, [sp, -48]! ; prologue junk
	add	x29, sp, 0
	str	w0, [x29, 28] ; your input first loaded in
	str	x1, [x29, 16]
	ldr	x0, [x29, 16]
	add	x0, x0, 8
	ldr	x0, [x0]
	bl	atoi
	bl	func1
	str	w0, [x29, 44]
	adrp	x0, .LC0
	add	x0, x0, :lo12:.LC0
	ldr	w1, [x29, 44]
	bl	printf ; prints result, flag format truncates anser to ed2c0662
	nop
	ldp	x29, x30, [sp], 48
	ret
	.size	main, .-main
	.ident	"GCC: (Ubuntu/Linaro 7.5.0-3ubuntu1~18.04) 7.5.0"
	.section	.note.GNU-stack,"",@progbits
