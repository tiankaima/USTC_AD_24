// F(0) = 7 , F(1) = 11, F(n) = F(n-1) + F(n-2) for n > 1

fn f(n: u32) -> u32 {
    if n == 0 {
        7
    } else if n == 1 {
        11
    } else {
        f(n - 1) + f(n - 2)
    }
}

fn main() {
    loop {
        // read input
        let mut input = String::new();
        std::io::stdin().read_line(&mut input).unwrap();
        let n: u32 = input.trim().parse().unwrap();
        // print yes if F(n) % 3 == 0
        if f(n) % 3 == 0 {
            println!("yes");
        } else {
            println!("no");
        }
    }
}