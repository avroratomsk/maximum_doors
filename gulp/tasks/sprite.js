import svgSprite from "gulp-svg-sprite";

export const sprite = () => {
	return app.gulp.src(`${app.path.src.svgicons}`, {})
		.pipe(app.plugins.plumber(
			app.plugins.notify.onError({
				title: "SVG",
				message: "Error: <%= error.message %>"
			}))
		)
		.pipe(svgSprite({
			mode: {
				symbol: {
					sprite: '../img/icons/icons.svg',
					example: true
				}
			},

		}))
		.pipe(app.gulp.dest(`${app.path.build.images}`));
}

export const spriteAdmin = () => {
	return app.gulp.src(`${app.pathAdmin.src.svgicons}`, {})
		.pipe(app.plugins.plumber(
			app.plugins.notify.onError({
				title: "SVG",
				message: "Error: <%= error.message %>"
			}))
		)
		.pipe(svgSprite({
			mode: {
				symbol: {
					sprite: '../img/icons/icons.svg',
					example: true
				}
			},

		}))
		.pipe(app.gulp.dest(`${app.pathAdmin.build.images}`));
}