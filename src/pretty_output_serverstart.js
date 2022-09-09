import chalkAnimation from 'chalk-animation';
const rainbow = chalkAnimation.rainbow("Overwatch working in this directory...")
setTimeout(() => {
	rainbow.start()
}, 1000);

setTimeout(() => {
	rainbow.stop()
}, 1000);
