var path = require('path');

var paths = {
  js: {},
  styles: {
    src: path.resolve(__dirname, './{{ cookiecutter.app_name }}/apps/static/sass'),
    src_files: path.resolve(__dirname, './{{ cookiecutter.app_name }}/apps/static/sass/**/*.scss'),
    dst: path.resolve(__dirname, './{{ cookiecutter.app_name }}/apps/static/css'),
    dst_filename: 'style.css'
  }
}

module.exports = paths;
