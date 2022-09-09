import chalkAnimation from 'chalk-animation';

const rainbow = chalkAnimation.rainbow("Overwatch has detected a change in the project...")
const build = chalkAnimation.rainbow("building...")

setTimeout(() => {
	rainbow.start()
	build.start()
}, 1000);

setTimeout(() => {
	rainbow.stop()
	build.stop()
}, 1000);
