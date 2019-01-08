#[macro_use]
extern crate clap;

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
struct BloodPressure {
    systolic: u32,
    diastolic: u32
}

impl BloodPressure {
    fn new(systolic: u32, diastolic: u32) -> BloodPressure {
        return BloodPressure { systolic, diastolic }
    }
}

/// Classifies a blood pressure reading
fn classify_blood_pressure(blood_pressure: BloodPressure) -> BloodPressureCategory {
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
        .about("Classify your blood pressure.")
        .version(version.as_str())
        .global_setting(AppSettings::ColoredHelp)
        .global_setting(AppSettings::UnifiedHelpMessage)
        .global_setting(AppSettings::VersionlessSubcommands)
        .arg(Arg::with_name("systolic")
            .required(true)
            .help("The systolic blood pressure reading in mmHg"))
        .arg(Arg::with_name("diastolic")
            .required(true)
            .help("The diastolic blood pressure reading in mmHg"))
        .get_matches();

    let systolic = matches.value_of("systolic").unwrap().parse::<u32>().unwrap();
    let diastolic = matches.value_of("diastolic").unwrap().parse::<u32>().unwrap();
    println!("{:?}", classify_blood_pressure(BloodPressure::new(systolic, diastolic)));
}
