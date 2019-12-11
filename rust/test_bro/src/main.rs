use std::io;


fn main() {
    let mut bob = String::new();


    println!("enter 1, 2 or 3");
    match io::stdin().read_line(&mut bob) {
        Ok(_) => {
            if bob == String::from("1\n") {
                println!("thing 1");
                return;
            }
            else if bob == String::from("2\n") {
                println!("thing 2");
                return;
            }
            else if bob == String::from("3\n") {
                println!("thing 3");
                return;
            }
            else {
                println!("the option '{0}' is invalid. Please enter 1, 2 or 3", bob);
                return;
            }
        },
        Err(e) => println!("wtf did you do to cause this: {}", e)
    }
}
