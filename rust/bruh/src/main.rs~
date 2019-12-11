use std::f64;


fn main() {
    let pi = 3.14159265359;
    let x = 5_f32*pi;
    

    let a = 1.0;
    let b = 3.0;
    let c = 2.0;


    if x != 4_f32*pi {
        qf(a, b, c);
    }
    else if x==4_f32*pi {
        println!("Fuck off, but pi is {:.*} to 5 dp", 5, pi);
    }
}

fn qf(a:f64,b:f64,c:f64) -> () {
    let disc = (b*b)-4_f64*a*c;
    

    if disc < 0_f64 {
        println!("No real roots");
    }
    else {
        let _x1 = (-b+disc.sqrt()) / (2_f64*a);
        let _x2 = (-b-disc.sqrt()) / (2_f64*a);
    

        println!("X is {0} and {1}", _x1, _x2);
    }
}
