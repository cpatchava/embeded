	.arch armv5t
	.fpu softvfp
	.eabi_attribute 20, 1
	.eabi_attribute 21, 1
	.eabi_attribute 23, 3
	.eabi_attribute 24, 1
	.eabi_attribute 25, 1
	.eabi_attribute 26, 2
	.eabi_attribute 30, 6
	.eabi_attribute 34, 0
	.eabi_attribute 18, 4
	.file	"hw1.cpp"
	.global	p      							#This is where the stack is setting up the global variable p
	.bss
	.align	2
	.type	p, %object
	.size	p, 4
p:
	.space	4
	.text
	.align	2
	.global	main
	.type	main, %function
main:
	.fnstart
.LFB0:
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 1, uses_anonymous_args = 0
	@ link register save eliminated.
	str	fp, [sp, #-4]!
	add	fp, sp, #0
.L2:
	ldr	r3, .L3								#load into r3 the pointer which is p
	ldr	r3, [r3, #0]						#load into r3 the value at r3+0
	mov	r2, #1								#place the value 1 into r2
	str	r2, [r3, #0]						#store r2, at r3 + 0
	ldr	r3, .L3								#load into r3 the pointer which is p
	ldr	r3, [r3, #0]						#load into r3 the value at r3 + 0
	mov	r2, #0								place the value 0 into r2
	str	r2, [r3, #0]						#store r2, at r3 + 0
	b	.L2									#jump to .L2 (beginning of loop)
.L4:
	.align	2
.L3:
	.word	p
	.cantunwind
	.fnend
	.size	main, .-main
	.ident	"GCC: (Ubuntu/Linaro 4.7.3-12ubuntu1) 4.7.3"
	.section	.note.GNU-stack,"",%progbits
