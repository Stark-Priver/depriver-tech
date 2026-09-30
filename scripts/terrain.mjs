// Generates the topographic "terrain" artwork (same look as the carousels):
// public/terrain-light.svg + public/terrain-dark.svg as cached backgrounds, and src/data/hero-lines.json
// (a lighter set drawn inline in the hero so it can animate).
import { contours } from "d3-contour";
import { createNoise2D } from "simplex-noise";
import { writeFileSync } from "node:fs";

function mulberry32(a) {
  return () => {
    a |= 0; a = (a + 0x6d2b79f5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

function field(seed, w, h, scale) {
  const noise = createNoise2D(mulberry32(seed));
  const values = new Float64Array(w * h);
  for (let y = 0; y < h; y++)
    for (let x = 0; x < w; x++) {
      const nx = x / scale, ny = y / scale;
      values[y * w + x] = noise(nx, ny) + 0.5 * noise(nx * 2.1, ny * 2.1) + 0.22 * noise(nx * 4.3, ny * 4.3);
    }
  return values;
}

function paths(seed, w, h, scale, levels, unit) {
  const values = field(seed, w, h, scale);
  const thresholds = Array.from({ length: levels }, (_, i) => -1.5 + (3 * (i + 0.5)) / levels);
  return contours().size([w, h]).smooth(true).thresholds(thresholds)(values).map((c, i) => ({
    major: i % 5 === 0,
    d: c.coordinates
      .flat()
      .map((ring) => "M" + ring.map(([x, y]) => `${(x * unit).toFixed(0)},${(y * unit).toFixed(0)}`).join("L") + "Z")
      .join(""),
  }));
}

function svg({ w, h, list }, stroke, majorStroke, width) {
  const body = list
    .map((p) => `<path d="${p.d}" stroke="${p.major ? majorStroke : stroke}" stroke-width="${p.major ? width * 1.6 : width}"/>`)
    .join("");
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${w} ${h}" preserveAspectRatio="xMidYMid slice" fill="none">${body}</svg>`;
}

const root = new URL("../", import.meta.url);
const light = { w: 1600, h: 1000, list: paths(7, 161, 101, 55, 24, 10) };
const dark = { w: 1600, h: 1000, list: paths(31, 161, 101, 45, 20, 10) };
writeFileSync(new URL("public/terrain-light.svg", root), svg(light, "#D5DBE7", "#C3CCDD", 1.3));
writeFileSync(new URL("public/terrain-dark.svg", root), svg(dark, "#1C3563", "#264476", 1.3));
const hero = { w: 800, h: 1000, paths: paths(12, 41, 51, 26, 9, 20) };
writeFileSync(new URL("src/data/hero-lines.json", root), JSON.stringify(hero));
console.log("terrain artwork written");
