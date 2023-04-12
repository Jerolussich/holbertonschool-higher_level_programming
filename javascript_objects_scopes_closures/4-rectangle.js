#!/usr/bin/node

module.exports =
    class Rectangle {
      constructor (w, h) {
        if (parseInt(w) > 0 && parseInt(h) > 0) {
          this.width = w;
          this.height = h;
        }
      }

      print() {
        for (let i = 0; i < this.height; i++) {
          for (let i = 0; i < this.width; i++) {
            process.stdout.write('X');
          }
          console.log('');
        }
      }

      rotate() {
        [this.width, this.height] = [this.height, this.width];
      }

      double() {
        this.height *= 2;
        this.width *= 2;
      }
    };
