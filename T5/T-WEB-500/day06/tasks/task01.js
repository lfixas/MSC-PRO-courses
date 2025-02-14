export function drawTriangle(height) {
    for (let h = 1; h <= height; h++) {
        process.stdout.write('$'.repeat(h) + '\n');
    }
}
