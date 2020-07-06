var THREE = require('three');
var OrbitControls = require('three-orbitcontrols');

var camera, scence, renderer, controls;

var init = function () {
  const canvas = document.getElementById('c');
  renderer = new THREE.WebGLRenderer({canvas});
  camera = new THREE.PerspectiveCamera( 70, window.innerWidth / window.innerHeight, 1, 1000);
  camera.up.set( 0, 0, 1 );
  camera.position.z = 15;
  camera.position.x = 4;
  
  controls = new OrbitControls(camera, renderer.domElement);
  controls.target.set(4, 6, 0);
  controls.update();
  
  scene = new THREE.Scene();
  scene.background = new THREE.Color( 0xffffff );
    
  const light = new THREE.DirectionalLight(0xFFFFFF, 1.2);
  light.position.set(4, 10, 6);
  scene.add(light);
  
  var base = makeBase();
  var pixels = pixelSetup();
}

var animate = function () {
  requestAnimationFrame( animate );
  
  if (resizeRendererToDisplaySize(renderer)) {
    const canvas = renderer.domElement;
    camera.aspect = canvas.clientWidth / canvas.clientHeight;
    camera.updateProjectionMatrix();
  }
  
  renderer.render( scene, camera );
};

var makeInstance = function (geometry, color, x_pos, y_pos, z_pos) {
  var material = new THREE.MeshPhongMaterial({color: color});
  var cube = new THREE.Mesh( geometry, material );
  scene.add(cube);
  cube.position.x = x_pos;
  cube.position.y = y_pos;
  cube.position.z = z_pos;
  return cube;
}

var resizeRendererToDisplaySize = function (renderer) {
  const canvas = renderer.domElement;
  const pixelRatio = window.devicePixelRatio;
  const width  = canvas.clientWidth  * pixelRatio | 0;
  const height = canvas.clientHeight * pixelRatio | 0;
  const needResize = canvas.width !== width || canvas.height !== height;
  if (needResize) {
    renderer.setSize(width, height, false);
  }
  return needResize;
}

function makeBase() {
  var base_geometry = new THREE.BoxGeometry(8, 12, 0.25);
  var base2_geometry = new THREE.BoxGeometry(8.5, 12.5, 0.5);
  
  var base = makeInstance(base_geometry, 0x44aa88, 4, 6,0);
  var base2 = makeInstance(base2_geometry, 0x44aa88, 4, 6,4.7);
  
  scene.add( base );
  scene.add( base2 )
  return base;
}

function pixelSetup() {
  var rod_geometry = new THREE.BoxGeometry(0.9, 0.9, 5);
  var pixels = [];
  
  for (var i = 0; i < 8; i++) {
    for (var j=0; j< 12; j++) {
      pixels.push(makeInstance(rod_geometry, 0xFF0000, i+0.5,j+0.5,2.5));
    }
  }
  return pixels;
}

init();
animate();