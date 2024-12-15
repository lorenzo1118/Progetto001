#include <iostream>  // Include la libreria che permette di utilizzare input e output standard

using namespace std;  // Usa il namespace standard, per evitare di scrivere "std::" ogni volta

// Funzione che calcola la somma dei numeri da 1 a N
int somma_interi(int N) {
    int somma = 0;  // Inizializziamo la variabile somma a 0
    // Ciclo che va da 1 a N (incluso) per sommare i numeri
    for (int i = 1; i <= N; ++i) {
        somma += i;  // Aggiungiamo i ad ogni passo alla variabile somma
    }
    return somma;  // Restituiamo il risultato della somma
}

int main() {
    int N = 100;  // Impostiamo il valore di N a 100. Vogliamo sommare i numeri da 1 a 100

    // Chiamiamo la funzione somma_interi passando N come parametro, e salviamo il risultato in 'risultato'
    int risultato = somma_interi(N);

    // Stampiamo il risultato della somma sullo schermo
    cout << "La somma dei numeri da 1 a " << N << " è: " << risultato << endl;

    return 0;  // Indica che il programma è terminato con successo
}
