import argparse
import utils.utils as utils


def main():
    parser = argparse.ArgumentParser(prog='test.py')
    parser.add_argument('--path', type=str, default='data/kitti_training_files_train.txt', help='path to training text file')
    parser.add_argument('--num_clusters', type=int, default=9, help='number of kmeans clusters')
    opt = parser.parse_args()

    anchors_list = utils.kmean_anchors(path=opt.path, n=opt.num_clusters, img_size=(608, 608))

    print("Anchors list for '%s': %s" % (opt.path, anchors_list))


if __name__ == '__main__':
    main()
