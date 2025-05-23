import fileinclude from "gulp-file-include"
import webpHtmlNosvg from "gulp-webp-html-nosvg"
import versionNumber from "gulp-version-number"

export const html = () => {
  return app.gulp.src(app.path.src.html)
    .pipe(app.plugins.plumber(
      app.plugins.notify.onError({
        title: "HTML",
        message: "Error: <%= error.message %>"
      })
    ))
    .pipe(fileinclude())
    .pipe(app.plugins.replace(/@img\//g, 'img/'))
    .pipe(webpHtmlNosvg())
    // .pipe(versionNumber({
    //   'value': '%DT%',
    //   'append': {
    //     'key': '_v',
    //     'cover': 1,
    //     'to': [
    //       'css',
    //       'js'
    //     ]
    //   },
    //   'output': {
    //     'file': 'gulp/version.json'
    //   }
    // }))
    .pipe(app.gulp.dest(app.path.build.html))
    .pipe(app.plugins.browsersync.stream())
}

export const htmlAdmin = () => {
  return app.gulp.src(app.pathAdmin.src.html)
    .pipe(app.plugins.plumber(
      app.plugins.notify.onError({
        title: "HTML",
        message: "Error: <%= error.message %>"
      })
    ))
    .pipe(fileinclude())
    .pipe(app.plugins.replace(/@img\//g, 'img/'))
    .pipe(webpHtmlNosvg())
    // .pipe(versionNumber({
    //   'value': '%DT%',
    //   'append': {
    //     'key': '_v',
    //     'cover': 1,
    //     'to': [
    //       'css',
    //       'js'
    //     ]
    //   },
    //   'output': {
    //     'file': 'gulp/version.json'
    //   }
    // }))
    .pipe(app.gulp.dest(app.pathAdmin.build.html))
    .pipe(app.plugins.browsersync.stream())
}