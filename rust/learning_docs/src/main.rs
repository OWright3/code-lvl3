use std::io;
use std::cmp::Ordering;
use rand::Rng;

fn main() {
    println!("The number is between 1 and 10: ");


    let mut input = String::new();
    
    
    io::stdin()
        .read_line(&mut input)
        .expect("wrong");


    let input: u32 = input
        .trim()
        .parse()
        .expect("Please type a number");

    println!("Your guess is: {}", input);
    

    let num = rand::thread_rng()
        .gen_range(1, 10);


    match input.cmp(&num) {
        Ordering::Less => println!("Too small!"),
        Ordering::Greater => println!("Too big!"),
        Ordering::Equal => println!("You win!"),
    }
}

//Guessing game section of the main rust book