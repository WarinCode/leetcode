/**
 * @param {number} millis
 * @return {Promise}
 */
async function sleep(millis) {
    return new Promise(res => setTimeout(res, millis))
}

sleep(1000).then(() => console.log(1))
sleep(2000).then(() => console.log(2))
sleep(3000).then(() => console.log(3))
sleep(4000).then(() => console.log(4))
sleep(5000).then(() => console.log(5))