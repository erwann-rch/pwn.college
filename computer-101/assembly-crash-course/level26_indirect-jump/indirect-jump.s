.intel_syntax noprefix
.global _start
_start:
    cmp rdi, 3
    jnbe default
    jmp [rsi + rdi * 8]
 default:
    jmp [rsi + 4 * 8]