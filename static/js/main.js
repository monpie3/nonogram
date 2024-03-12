import * as THREE from 'three';
import { DragControls } from 'https://unpkg.com/three/examples/jsm/controls/DragControls.js';

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);

const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

const geometry = new THREE.BoxGeometry(1, 1, 1);
const material = new THREE.MeshBasicMaterial({ color: 0x00ff00 });
const cube = new THREE.Mesh(geometry, material);
scene.add(cube);

camera.position.z = 5;

const controls = new DragControls([cube], camera, renderer.domElement);

controls.addEventListener('dragstart', function (event) {
    event.object.material.color.set(0xc96b65);
});

controls.addEventListener('dragend', function (event) {
    event.object.material.color.set(0xf21505);
});


function animate() {

    requestAnimationFrame(animate);

    cube.rotation.x += 0.01;
    cube.rotation.y += 0.01;

    renderer.render(scene, camera);

}

animate();
