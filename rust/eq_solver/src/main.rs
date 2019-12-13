use std::f64;
use std::io;

fn main() {
    let pi = 3.14159265359;
    let x = 5_f32*pi;
    let mut count = 0.0;

    loop  {
        let a = input("enter a value for 'a': ").unwrap().parse::<f64>().expect("expected a number");
        let b = input("enter a value for 'b': ").unwrap().parse::<f64>().expect("expected a number");
        let c = input("enter a value for 'c': ").unwrap().parse::<f64>().expect("expected a number");


        if x != 4_f32 * pi {
            qf(a, b, c);
        } else if x == 4_f32 * pi {
            println!("Fuck off, but pi is {:.*} to 5 dp", 5, pi);
        }
        count += 1.0;


        if count == 5.0 {
            println!("Enough!");
            break;
        }
    }
}

fn qf(a:f64,b:f64,c:f64) -> () {
    let disc = (b*b)-4_f64*a*c;


    if disc < 0_f64 {
        println!("No real roots");
    }
    else {
        let s_x1 = (-b+disc.sqrt()) / (2_f64*a);
        let s_x2 = (-b-disc.sqrt()) / (2_f64*a);
        let b_x1 = -(s_x1);
        let b_x2 = -(s_x2);

        println!("X is {0} and {1}", s_x1, s_x2);

        println!("(x + {0})(x + {1})", b_x1, b_x2);
    }
}

fn input(user_message: &str) -> io::Result<String> {
    use std::io::Write;

    print!("{}", user_message);

    // flush forces the print statement to the display.
    io::stdout().flush()?;

    let mut buffer: String = String::new();
    io::stdin().read_line(&mut buffer)?;

    Ok(buffer.trim_end().to_owned())
}
