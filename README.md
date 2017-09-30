# math113_auto_latex

This is a script to automatically generate LaTeX code in the format I usually use for weekly homework assignments in Math 113: Introduction to Abstract Algebra at UC Berkeley. Given the exercise numbers in a specific format, the write_latex function writes LaTeX code to a temporary file so it can be copy and pasted into a LaTeX document.

## Example

Input:  
"Exercises 10: 4, 6, 12, 16, 20, 22, 24, 39, 40, 41, 43, 44  
Exercises 11: 14, 16, 22, 39, 47, 49, 50, 53"

Output:  
A text file formatted like this:  
\section{Textbook Exercises}  
\begin{mdframed}  
\textbf{10.4}  
  
  
\end{mdframed}  
  
\begin{mdframed}  
\textbf{10.6}  
  
  
\tend{mdframed}  
  
...  
  
\begin{mdframed}  
\textbf{11.53}  
  
  
\end{mdframed}  
