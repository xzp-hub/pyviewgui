use image::GenericImageView;
use pyo3::prelude::*;
use pyo3::types::PyModule;
use pyo3::Bound;
use std::fs::read_to_string;
use tao::window::Icon;
use tao::{
    event::{Event, WindowEvent},
    event_loop::{ControlFlow, EventLoop},
    window::WindowBuilder,
};
use wry::WebViewBuilder;

#[pyfunction]
pub fn py_create_window(
    win_title: String,
    win_width: u32,
    win_height: u32,
    win_content: String,
    win_icon_path: String,
    win_is_decorations: bool,
    win_is_resizable: bool,
    win_is_devtools: bool,
) {
    create_window(
        win_title,
        win_width,
        win_height,
        win_content,
        win_icon_path,
        win_is_decorations,
        win_is_resizable,
        win_is_devtools,
    );
}


#[pymodule]
#[pyo3(gil_used=false)]
fn _pyviewgui(_py: Python<'_>, m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(py_create_window, m)?)?;
    Ok(())
}

fn load_icon_from_path(path: &str) -> Option<Icon> {
    match image::open(path) {
        Ok(img) => {
            let (width, height) = img.dimensions();
            let rgba = img.to_rgba8();
            let raw_pixels: Vec<u8> = rgba.into_raw();
            Some(Icon::from_rgba(raw_pixels, width, height).unwrap())
        }
        Err(_) => None,
    }
}

pub fn create_window(
    win_title: String,
    win_width: u32,
    win_height: u32,
    win_content: String,
    win_icon_path: String,
    win_is_decorations: bool,
    win_is_resizable: bool,
    win_is_devtools: bool,
) {
    let event_loop = EventLoop::new();

    let window = WindowBuilder::new()
        .with_title(win_title)
        .with_inner_size(tao::dpi::LogicalSize::new(win_width, win_height))
        .with_decorations(win_is_decorations)
        .with_resizable(win_is_resizable)
        .with_window_icon(load_icon_from_path(&win_icon_path))
        .build(&event_loop);

    match window {
        Ok(window) => {
            match if win_content.starts_with("http") {
                WebViewBuilder::new()
                    .with_url(win_content)
                    .with_devtools(win_is_devtools)
                    .build(&window)
            } else {
                WebViewBuilder::new()
                    .with_html(read_to_string(win_content).expect("Failed to read html file"))
                    .with_devtools(win_is_devtools)
                    .build(&window)
            } {
                Ok(_) => event_loop.run(move |event, _, control_flow| {
                    *control_flow = ControlFlow::Wait;
                    match event {
                        Event::WindowEvent {
                            event: WindowEvent::CloseRequested,
                            ..
                        } => *control_flow = ControlFlow::Exit,
                        _ => {}
                    }
                }),
                Err(err) => panic!("Failed to create webview: {}", err),
            }
        }
        Err(err) => panic!("Failed to create window: {}", err),
    }
}
