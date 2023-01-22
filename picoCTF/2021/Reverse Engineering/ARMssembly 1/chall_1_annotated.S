# Consider this to be a write-up
################################# Write-Up ####################################
# Challenge: ARMssembly 1
# Category: Reverse Engineering
# Description: For what argument does this program print `win` with variables 79, 7 and 3? File: chall_1.S Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})
# Hints:
#	-1: Shifts
#
# Flag: picoCTF{00000d2a}
# Points: 70
# Solved in picoGym

	.arch armv8-a
	.file	"chall_1.c"
	.text
	.align	2
	.global	func
	.type	func, %function
func:
	sub	sp, sp, #32 ; prologue
	str	w0, [sp, 12] ; our argument stored in [sp + 12]
	mov	w0, 79 ; w0 = 79
	str	w0, [sp, 16] ; 79 in [sp + 16]
	mov	w0, 7 ; w0 = 7
	str	w0, [sp, 20] ; 7 in [sp + 20]
	mov	w0, 3 ; w0 = 3
	str	w0, [sp, 24] ; 3 in [sp + 24]
	ldr	w0, [sp, 20] ; w0 = 7
	ldr	w1, [sp, 16] ; w1 = 79
	lsl	w0, w1, w0 ; left shift, hint alludes to this, remember w registers hold 32 bits, basically w0 = w1 << w0 = 79 << 7 = 0000000000000000000001001111 << 7 = 10112
	str	w0, [sp, 28] ; 10112 in [sp + 28]
	ldr	w1, [sp, 28] ; w1 = 10112
	ldr	w0, [sp, 24] ; w0 = 3
	sdiv	w0, w1, w0 ; w0 = w1 / w0 = 10112 / 3 = 3370 (remember it's truncated)
	str	w0, [sp, 28] ; 3370 stored in [sp + 28]
	ldr	w1, [sp, 28] ; w1 = 3370
	ldr	w0, [sp, 12] ; w0 = our argument
	sub	w0, w1, w0 ; w0 = 3370 - our argument
	str	w0, [sp, 28] ; result stored in [sp + 28]
	ldr	w0, [sp, 28] ; w0 = result
	add	sp, sp, 32 ; eplilogue
	ret
	.size	func, .-func
	.section	.rodata
	.align	3 ; gist of func: return 3370 - our argument
.LC0:
	.string	"You win!" ; our goal
	.align	3
.LC1:
	.string	"You Lose :("
	.text
	.align	2
	.global	main
	.type	main, %function
main:
	stp	x29, x30, [sp, -48]! ; prologue
	add	x29, sp, 0
	str	w0, [x29, 28] 
	str	x1, [x29, 16]
	ldr	x0, [x29, 16] ; making our argument readable as an integer
	add	x0, x0, 8
	ldr	x0, [x0]
	bl	atoi
	str	w0, [x29, 44] ; load in our argument
	ldr	w0, [x29, 44]
	bl	func ; call func
	cmp	w0, 0 ; key cmp: checks if func(<our argument>) = 0
	bne	.L4 ; if not we lose
	adrp	x0, .LC0 ; if so we win, so 3370 - <our argument> = 0 to win
	add	x0, x0, :lo12:.LC0
	bl	puts
	b	.L6 ; epilogue
.L4:
	adrp	x0, .LC1
	add	x0, x0, :lo12:.LC1
	bl	puts
.L6:
	nop
	ldp	x29, x30, [sp], 48
	ret
	.size	main, .-main
	.ident	"GCC: (Ubuntu/Linaro 7.5.0-3ubuntu1~18.04) 7.5.0"
	.section	.note.GNU-stack,"",@progbits

; Our result: argument must be 3370 to win, 0xd2a in hex
