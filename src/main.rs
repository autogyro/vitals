#[macro_use]
extern crate clap;
extern crate chrono;

mod files;

use chrono::Local;
use clap::{Arg, App, AppSettings};

#[derive(Debug)]
enum BloodPressureCategory {
    Normal,
    Elevated,
    High1,
    High2,
    Crisis
}

#[derive(Debug)]
enum PulseCategory {
    Low,
    Normal,
    High
}

#[derive(Debug)]
struct BloodPressureReading {
    systolic: u32,
    diastolic: u32,
    pulse: u32
}

impl BloodPressureReading {
    fn new(systolic: u32, diastolic: u32, pulse: u32) -> BloodPressureReading {
        return BloodPressureReading { systolic, diastolic, pulse }
    }
}

/// Classifies a pulse reading
fn classify_pulse(blood_pressure: &BloodPressureReading) -> PulseCategory {
    if blood_pressure.pulse < 60 {
        return PulseCategory::Low;
    } else if blood_pressure.pulse > 100 {
        return PulseCategory::High;
    } else {
        return PulseCategory::Normal;
    }
}

/// Classifies a blood pressure reading
fn classify_blood_pressure(blood_pressure: &BloodPressureReading) -> BloodPressureCategory {
    if blood_pressure.systolic < 120 && blood_pressure.diastolic < 80 {
        return BloodPressureCategory::Normal;
    } else if blood_pressure.systolic < 130 && blood_pressure.diastolic < 80 {
        return BloodPressureCategory::Elevated
    } else if blood_pressure.systolic < 140 || blood_pressure.diastolic < 90 {
        return BloodPressureCategory::High1
    } else if blood_pressure.systolic > 180 || blood_pressure.diastolic > 120 {
        return BloodPressureCategory::Crisis
    } else {
        return BloodPressureCategory::High2
    }
}

fn main() {
    let version = format!("{}", crate_version!());
    let matches = App::new("blood_pressure")
        .about("Log your blood pressure.")
        .version(version.as_str())
        .global_setting(AppSettings::ColoredHelp)
        .global_setting(AppSettings::UnifiedHelpMessage)
        .global_setting(AppSettings::VersionlessSubcommands)
        .arg(Arg::with_name("systolic")
            .required(true)
            .help("Your systolic blood pressure reading in mmHg"))
        .arg(Arg::with_name("diastolic")
            .required(true)
            .help("Your diastolic blood pressure reading in mmHg"))
        .arg(Arg::with_name("pulse")
            .required(true)
            .help("Your pulse in bpm"))
        .get_matches();

    // Read vitals from command line
    // let time = SystemTime::now().duration_since(UNIX_EPOCH).unwrap().as_millis();
    let now = Local::now();
    let date = now.format("%Y-%m-%d");
    let time = now.format("%H:%M:%S");
    let systolic = matches.value_of("systolic").unwrap().parse::<u32>().unwrap();
    let diastolic = matches.value_of("diastolic").unwrap().parse::<u32>().unwrap();
    let pulse = matches.value_of("pulse").unwrap().parse::<u32>().unwrap();

    // Open/create vitals.csv

    // If file is empty, write csv headers
    let data_len = files::read("vitals.csv").unwrap().len();

    if data_len == 0 {
        files::append("vitals.csv", "date,time,systolic,diastolic,pulse\n").unwrap();
    }

    // Write to file in CSV format
    files::append("vitals.csv", format!("{},{},{},{},{}\n", date, time, systolic, diastolic, pulse)).unwrap();

    // Display information about the last vitals log (blood pressure classification, heart rate classification)
    let blood_pressure_reading = BloodPressureReading::new(systolic, diastolic, pulse);

    println!("Blood pressure category: {:?}", classify_blood_pressure(&blood_pressure_reading));
    println!("Pulse category: {:?}", classify_pulse(&blood_pressure_reading));
}
