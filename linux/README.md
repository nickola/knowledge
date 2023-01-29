# Linux

Linux is open-source Unix-like operating systems (OS) based on the Linux kernel.
Linux kernel was first released in 1991 by Linus Torvalds.

## Load Average (LA)

`Load Average` (LA) represents the average system load – the number of processes executed by the CPU or are waiting for execution.
It is displayed for a period of time (`1`, `5` and `15` minutes) in the output of the `uptime` or `top` commands.

It can be also checked using `proc` filesystem: `cat /proc/loadavg`. The first three columns is `Load Average`.
The fourth column shows the number of currently running processes and the total number of processes.
The last column displays the last process ID used.

## "proc" Filesystem

The `proc` filesystem (`procfs`) is a special filesystem in Unix-like operating systems that presents information about processes
and other system information in a hierarchical file-like structure.

## Process States

Linux process states:
  - `R` (running or runnable): On run queue, waiting for the CPU.
  - `S` (interruptible sleep): Waiting for an event, such as input from the terminal.
  - `D` (uninterruptible sleep): Usually IO, cannot be killed or interrupted with a signal.
  - `Z` (zombie / defunct): Terminated but its exit status is not read by parent process yet.
