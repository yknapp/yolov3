import argparse
import re
import matplotlib.pyplot as plt


def read_txt_file(path):
    with open(path) as f:
        return f.readlines()


def search_reg(file_content, regex):
    file_content_str = '\n'.join(file_content)
    p = re.compile(regex)
    return p.findall(file_content_str)


def create_plot(array, title, label, xlabel, ylabel):
    x_labels = [(x+1)*1000 for x in range(len(array))]
    plt.plot(x_labels, array, label=label)
    #plt.ylim([0, 1])
    #plt.yscale('log')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend(loc="upper right")
    plt.title(title)


def show_curr_plot():
    plt.show()


def save_curr_plot(output_filename):
    plt.savefig(output_filename, dpi=300)


def main():
    #parser = argparse.ArgumentParser()
    #parser.add_argument('--evaluation_file', type=str, default=None, help="file containing all ComplexYOLO evaluation results")
    #opts = parser.parse_args()
    evaluation_file = "/home/user/work/master_thesis/code/UNIT/outputs/unit_fov_lyft2kitti/unit_fov_lyft2kitti.txt"
    #evaluation_file = "/home/user/work/master_thesis/code/UNIT/outputs/unit_fov_audi2kitti/unit_fov_audi2kitti.txt"

    file_content = read_txt_file(evaluation_file)
    dict_classes = dict()

    # extract metrics
    classes = ('all', 'Car', 'Pedestrian', 'Cyclist')
    for _class in classes:
        dict_classes[_class] = []
        for line in file_content:
            if line.strip().startswith(_class):
                line_subs = ' '.join(line.split()) # substitute multiple spaces with one space
                line_split = line_subs.split()
                # line_split indices: 3: precision, 4: recall, 5: map, 6: f1
                dict_classes[_class].append(float(line_split[5]))

    # print maxima
    extracted_mAPs_total = dict_classes[classes[0]]
    extracted_mAPs_car = dict_classes[classes[1]]
    extracted_mAPs_pedestrian = dict_classes[classes[2]]
    extracted_mAPs_cyclist = dict_classes[classes[3]]
    print("Max mAP: %s (idx %s)" % (max(extracted_mAPs_total), extracted_mAPs_total.index(max(extracted_mAPs_total))))
    print("Max car AP: %s (idx %s)" % (max(extracted_mAPs_car), extracted_mAPs_car.index(max(extracted_mAPs_car))))
    print("Max pedestrian AP: %s (idx %s)" % (max(extracted_mAPs_pedestrian), extracted_mAPs_pedestrian.index(max(extracted_mAPs_pedestrian))))
    print("Max cyclist AP: %s (idx %s)" % (max(extracted_mAPs_cyclist), extracted_mAPs_cyclist.index(max(extracted_mAPs_cyclist))))

    # create plot
    plot_title = "ComplexYOLO Performance"
    axis_label_x = "UNIT iterations"
    axis_label_y = "ComplexYOLO AP"
    create_plot(extracted_mAPs_total, plot_title, "mAP", axis_label_x, axis_label_y)
    create_plot(extracted_mAPs_car, plot_title, "car AP", axis_label_x, axis_label_y)
    create_plot(extracted_mAPs_pedestrian, plot_title, "pedestrian AP", axis_label_x, axis_label_y)
    create_plot(extracted_mAPs_cyclist, plot_title, "cyclist AP", axis_label_x, axis_label_y)
    show_curr_plot()
    #save_curr_plot("complexYOLO_eval.png")


if __name__ == '__main__':
    main()
