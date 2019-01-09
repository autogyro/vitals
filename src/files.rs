use std::path::{Path};
use std::io::{self, Write, Error, ErrorKind};
use std::fs::{self, OpenOptions};

fn create_all_dirs<P: AsRef<Path>>(path: P) -> io::Result<()> {
    match path.as_ref().parent() {
        Some(parent) => {
            fs::create_dir_all(&parent)
        },
        None => Err(Error::new(ErrorKind::Other, "Could not get parent directory"))
    }
}

// From https://github.com/pop-os/system76-power/blob/master/src/util.rs
pub fn append<P: AsRef<Path>, S: AsRef<[u8]>>(path: P, data: S) -> io::Result<()> {
    {
        create_all_dirs(&path)?;
        let mut file = OpenOptions::new().append(true).create(true).open(&path)?;
        file.write_all(data.as_ref())?
    }

    Ok(())
}

pub fn read<P: AsRef<Path>>(path: P) -> io::Result<String> {
    create_all_dirs(&path)?;
    OpenOptions::new().append(true).create(true).open(&path)?;
    Ok(fs::read_to_string(&path)?)
}
