use std::io;


fn main() {
    let ar: [i32; 11] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
    let mut f= 0; //if found f=1, otherwise f=0
    let i= 0; //index  
    
    println!("Please enter a number to search for in the array 'ar':\n")
    let mut s_term = String::new(); //numeric search term
    io::stdin()
        .read_line(&mut s_term)
        .expect("Not a search term");
    let s_term: i32 = s_term
        .trim()
        .parse()
        .expect("Please type a number");

  
    while f == 0 && i <= ar.len() - 1 {
        if ar[i] == s_term {
            f = 1;
        }
        else {
            i+1;
        }
    }


    if f == 1 {
        println!("Number: {0}, found at index: {1}.", s_term, i);
    }
    else {
        println!("Number: {0}, not found in array.", s_term);
    }
}
